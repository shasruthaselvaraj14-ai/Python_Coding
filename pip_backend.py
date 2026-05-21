from flask import Flask, request, render_template_string
import sqlite3

app = Flask(__name__)

# ==================================================
# DATABASE CREATION
# ==================================================

def create_database():

    conn = sqlite3.connect("college.db")
    cursor = conn.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS students (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            student_name TEXT,
            course TEXT,
            faculty_name TEXT,
            attendance TEXT,
            department_hod TEXT

        )

    """)

    cursor.execute("SELECT * FROM students")

    data = cursor.fetchone()

    if not data:

        cursor.execute("""

            INSERT INTO students
            (student_name, course, faculty_name, attendance, department_hod)

            VALUES (?, ?, ?, ?, ?)

        """, (

            "Shasrutha Selvaraj",
            "B.Tech Information Technology",
            "Reena",
            "92%",
            "Preethi"

        ))

    conn.commit()
    conn.close()


create_database()

# ==================================================
# LOGIN PAGE
# ==================================================

LOGIN_PAGE = """

<!DOCTYPE html>

<html>

<head>

    <title>Cyber Secure Portal</title>

    <style>

        *{
            margin:0;
            padding:0;
            box-sizing:border-box;
            font-family:Arial;
        }

        body{

            height:100vh;

            display:flex;
            justify-content:center;
            align-items:center;

            background:#020617;

            overflow:hidden;

            color:white;

        }

        /* Animated Grid */

        body::before{

            content:"";

            position:absolute;

            width:200%;
            height:200%;

            background-image:

            linear-gradient(rgba(0,255,255,0.05) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0,255,255,0.05) 1px, transparent 1px);

            background-size:50px 50px;

            animation:gridMove 10s linear infinite;

        }

        @keyframes gridMove{

            0%{
                transform:translate(0,0);
            }

            100%{
                transform:translate(-50px,-50px);
            }

        }

        .container{

            width:1100px;
            height:650px;

            display:flex;

            border-radius:25px;

            overflow:hidden;

            position:relative;

            z-index:1;

            background:rgba(15,23,42,0.75);

            backdrop-filter:blur(12px);

            box-shadow:0 0 40px rgba(0,255,255,0.4);

        }

        /* LEFT SIDE */

        .left{

            width:45%;

            padding:50px;

            display:flex;
            flex-direction:column;
            justify-content:center;

        }

        .logo{

            font-size:45px;
            margin-bottom:20px;

        }

        .heading{

            font-size:55px;
            font-weight:bold;

            background:linear-gradient(to right, cyan, violet);

            -webkit-background-clip:text;
            -webkit-text-fill-color:transparent;

            margin-bottom:15px;

        }

        .sub{

            color:#cbd5e1;

            margin-bottom:40px;

            font-size:18px;

        }

        .input-box{

            margin-bottom:25px;

        }

        .input-box label{

            display:block;

            margin-bottom:10px;

            color:#94a3b8;

        }

        .input-box input{

            width:100%;

            padding:15px;

            border:none;

            outline:none;

            border-radius:15px;

            background:#111827;

            color:white;

            font-size:16px;

        }

        .input-box input:focus{

            border:1px solid cyan;

            box-shadow:0 0 20px cyan;

        }

        .login-btn{

            width:100%;

            padding:15px;

            border:none;

            border-radius:15px;

            background:linear-gradient(90deg,#00d4ff,#8b5cf6);

            color:white;

            font-size:18px;

            font-weight:bold;

            cursor:pointer;

            transition:0.3s;

        }

        .login-btn:hover{

            transform:scale(1.03);

            box-shadow:0 0 25px cyan;

        }

        .footer{

            margin-top:30px;

            text-align:center;

            color:#94a3b8;

            font-size:14px;

        }

        /* RIGHT SIDE */

        .right{

            width:55%;

            display:flex;
            justify-content:center;
            align-items:center;

            position:relative;

        }

        .circle{

            width:420px;
            height:420px;

            border-radius:50%;

            padding:8px;

            background:linear-gradient(45deg, cyan, violet);

            animation:glow 3s infinite alternate;

        }

        @keyframes glow{

            from{
                box-shadow:0 0 20px cyan;
            }

            to{
                box-shadow:0 0 50px violet;
            }

        }

        .circle img{

            width:100%;
            height:100%;

            border-radius:50%;

            object-fit:cover;

            border:5px solid #020617;

        }

        .quote{

            position:absolute;

            bottom:60px;

            color:#e879f9;

            font-size:28px;

            font-style:italic;

        }

        .success{

            background:rgba(34,197,94,0.2);

            border:1px solid #22c55e;

            color:#22c55e;

            padding:12px;

            border-radius:12px;

            margin-bottom:20px;

            text-align:center;

            font-weight:bold;

        }

        .error{

            background:rgba(239,68,68,0.2);

            border:1px solid #ef4444;

            color:#ef4444;

            padding:12px;

            border-radius:12px;

            margin-bottom:20px;

            text-align:center;

            font-weight:bold;

        }

    </style>

</head>

<body>

<div class="container">

    <!-- LEFT -->

    <div class="left">

        <div class="logo">🔐</div>

        <div class="heading">
            Welcome Back!
        </div>

        <div class="sub">
            Login to Student IT Dashboard
        </div>

        {{ message|safe }}

        <form method="POST">

            <div class="input-box">

                <label>Username</label>

                <input type="text"
                       name="username"
                       placeholder="Enter Username"
                       required>

            </div>

            <div class="input-box">

                <label>Password</label>

                <input type="password"
                       name="password"
                       placeholder="Enter Password"
                       required>

            </div>

            <button class="login-btn">
                LOGIN
            </button>

        </form>

        <div class="footer">
            Cyber Security • Artificial Intelligence • IT Portal
        </div>

    </div>

    <!-- RIGHT -->

    <div class="right">

        <div class="circle">

            <!-- PUT YOUR IMAGE -->

            <img src="/static/myphoto.jpg">

        </div>

        <div class="quote">
            Stay Connected 💜
        </div>

    </div>

</div>

</body>

</html>

"""

# ==================================================
# DASHBOARD PAGE
# ==================================================

DASHBOARD_PAGE = """

<!DOCTYPE html>

<html>

<head>

    <title>Student Dashboard</title>

    <style>

        body{

            background:#020617;

            font-family:Arial;

            color:white;

            padding:40px;

        }

        h1{

            text-align:center;

            margin-bottom:40px;

            color:cyan;

        }

        .card{

            width:700px;

            margin:auto;

            background:#111827;

            padding:30px;

            border-radius:20px;

            box-shadow:0 0 25px rgba(0,255,255,0.3);

        }

        .row{

            margin-bottom:25px;

            padding:15px;

            border-radius:12px;

            background:#1e293b;

            font-size:20px;

        }

        .label{

            color:cyan;

            font-weight:bold;

        }

    </style>

</head>

<body>

    <h1>🎓 Student Information Dashboard</h1>

    <div class="card">

        <div class="row">
            <span class="label">Student Name :</span>
            {{ student_name }}
        </div>

        <div class="row">
            <span class="label">Course :</span>
            {{ course }}
        </div>

        <div class="row">
            <span class="label">Faculty Name :</span>
            {{ faculty_name }}
        </div>

        <div class="row">
            <span class="label">Attendance :</span>
            {{ attendance }}
        </div>

        <div class="row">
            <span class="label">Department HOD :</span>
            {{ department_hod }}
        </div>

    </div>

</body>

</html>

"""

# ==================================================
# LOGIN ROUTE
# ==================================================

@app.route("/", methods=["GET", "POST"])

def login():

    message = ""

    if request.method == "POST":

        username = request.form.get("username")
        password = request.form.get("password")

        # LOGIN DETAILS

        if username == "shasru" and password == "100514":

            conn = sqlite3.connect("college.db")
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM students")

            student = cursor.fetchone()

            conn.close()

            return render_template_string(

                DASHBOARD_PAGE,

                student_name=student[1],
                course=student[2],
                faculty_name=student[3],
                attendance=student[4],
                department_hod=student[5]

            )

        else:

            message = """

            <div class="error">

                Invalid Username or Password

            </div>

            """

    return render_template_string(
        LOGIN_PAGE,
        message=message
    )

# ==================================================
# RUN APPLICATION
# ==================================================

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
