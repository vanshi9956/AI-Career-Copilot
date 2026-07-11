from flask import Flask , render_template , request , redirect , session
from db import Base , engine, SessionLocal
import models
import PyPDF2
import docx
import json
from ai import analyze_resume
from werkzeug.security import generate_password_hash, check_password_hash
app=Flask(__name__)
app.secret_key="secret1234"
Base.metadata.create_all(bind=engine)
## HOME
@app.route("/")
def home():
    if "user" in session:  ## session means vo login hai uski info flask mein already hai
        return redirect("/dashboard")
    else:
        return redirect("/login")
    

#--> SIGNUP
@app.route("/signup" , methods=["GET" , "POST"]) 
def signup():
    db=SessionLocal()
    if request.method=='POST':
        email=request.form .get("email")

        password=request.form.get("password")

        existing_user=db.query(models.User).filter_by(email=email).first()
        if existing_user:
            return "User Already Exists"
        

        hashed_password = generate_password_hash(password)

        user = models.User(
        email=email,
        password=hashed_password
        ) 
        db.add(user)
        db.commit()
        return redirect("/login")
    return render_template("signup.html")


#--> LOGIN
@app.route("/login" , methods=["GET" ,"POST"]) 
def login():
    db=SessionLocal()
    if request.method=='POST': ## user ne send krne ke liye button click kr diya
        email=request.form.get("email")
        password=request.form.get("password")
        user=db.query(models.User).filter_by(email=email ).first()
        if user and check_password_hash(user.password, password):
            session["user"]=user.email
            return redirect("/dashboard")
        else:

            return "invalid credential"
    else:
        return render_template("/login.html")
    

#--> DASHBOARD
@app.route("/dashboard"  , methods=["GET" , "POST"])
def dashboard():
    if "user" not in session:
        return redirect("/login")
    
    result=None
    if request.method=='POST':
        user_role=request.form.get("role")
        resume_text=request.form.get("resume")

        file=request.files.get("file")

        ## file handling  -> converting my files into text resume

        if file and file.filename!="":
            if file.filename.endswith(".pdf"):
                try:
                  
                    pdf_reader=PyPDF2.PdfFileReader(file)
                    text=""
                    for page in pdf_reader.pages:
                        text+=page.extract_text() or ""
                    resume_text=text
                except Exception as e:
                    result={"error" :f"PDF :error{str(e)}"}
            elif file.filename.endswith(".docx"):
                try:
                    doc=docx.Document(file)
                    text=""
                    for para in doc.paragraphs:
                        text+=para.text+"\n"
                    resume_text=text

                except Exception as e:
                    result={"error: "f"DOCX: error {str(e)}"} 
        if resume_text and user_role:
            try:
                result=analyze_resume(resume_text , user_role)
                

                ## save to db
                db=SessionLocal()
                user=db.query(models.User).filter_by(email=session["user"]).first()

                ## adding to reports table
                report=models.Report(
                    user_id=user.id,
                    resume_text=resume_text,
                    result=json.dumps(result)
                )
                db.add(report)
                db.commit()
            except Exception as e:
                result={"error" : f"AI error: {str(e)}"}
   
           
    return render_template("dashboard.html" , user=session["user"] , result=result)

                    
@app.route("/history")
def history():
    if "user" not in session:
        return redirect("login")
    db=SessionLocal()
    user=db.query(models.User).filter_by(email=session["user"]).first()
    report=db.query(models.Report).filter_by(user_id=user.id).all()
    

    ## convert json to dic
    passed_report=[]
    for r in report:
        try:
            passed_result=json.loads(r.result)
        except:
            passed_result=[]
        passed_report.append({
            "resume": r.resume_text,
            "result": passed_result
        }

        )
    return render_template("history.html" , report=passed_report)


@app.route("/logout")
def logout():
    session.pop("user" , None)
    return redirect("/login")




print(app.url_map)



if __name__=="__main__":
    app.run(debug=True, use_reloader=False)
  

