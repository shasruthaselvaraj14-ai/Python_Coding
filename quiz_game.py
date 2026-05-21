def quiz():

questions = [
{
&quot;question&quot;: &quot;1. What is the output of: print(2+3)?&quot;,
&quot;options&quot;: [&quot;A. 23&quot;, &quot;B. 5&quot;, &quot;C. Error&quot;, &quot;D. None&quot;],
&quot;answer&quot;: &quot;B&quot;
},

{
&quot;question&quot;: &quot;2. Which symbol is used for comments in Python?&quot;,
&quot;options&quot;: [&quot;A. //&quot;, &quot;B. /* */&quot;, &quot;C. #&quot;, &quot;D. --&quot;],
&quot;answer&quot;: &quot;C&quot;
},

{
&quot;question&quot;: &quot;3. Which keyword is used to create a function?&quot;,
&quot;options&quot;: [&quot;A. func&quot;, &quot;B. define&quot;, &quot;C. def&quot;, &quot;D. function&quot;],
&quot;answer&quot;: &quot;C&quot;
},

{
&quot;question&quot;: &quot;4. Which data type stores True/False values?&quot;,

&quot;options&quot;: [&quot;A. int&quot;, &quot;B. bool&quot;, &quot;C. float&quot;, &quot;D. str&quot;],
&quot;answer&quot;: &quot;B&quot;
},

{
&quot;question&quot;: &quot;5. Which loop runs until condition becomes false?&quot;,
&quot;options&quot;: [&quot;A. for&quot;, &quot;B. while&quot;, &quot;C. if&quot;, &quot;D. switch&quot;],
&quot;answer&quot;: &quot;B&quot;
},

{
&quot;question&quot;: &quot;6. What is used to take input from user?&quot;,
&quot;options&quot;: [&quot;A. get()&quot;, &quot;B. input()&quot;, &quot;C. read()&quot;, &quot;D. scanf()&quot;],
&quot;answer&quot;: &quot;B&quot;
},

{
&quot;question&quot;: &quot;7. Which collection allows duplicate values?&quot;,
&quot;options&quot;: [&quot;A. set&quot;, &quot;B. dictionary&quot;, &quot;C. list&quot;, &quot;D. tuple&quot;],
&quot;answer&quot;: &quot;C&quot;
},

{
&quot;question&quot;: &quot;8. What is output of len(&#39;Python&#39;)?&quot;,
&quot;options&quot;: [&quot;A. 5&quot;, &quot;B. 6&quot;, &quot;C. 7&quot;, &quot;D. Error&quot;],

&quot;answer&quot;: &quot;B&quot;
},

{
&quot;question&quot;: &quot;9. Which operator is used for power?&quot;,
&quot;options&quot;: [&quot;A. ^&quot;, &quot;B. *&quot;, &quot;C. **&quot;, &quot;D. //&quot;],
&quot;answer&quot;: &quot;C&quot;
},

{
&quot;question&quot;: &quot;10. Python is a:&quot;,
&quot;options&quot;: [&quot;A. Programming Language&quot;, &quot;B. Browser&quot;, &quot;C. Database&quot;, &quot;D. OS&quot;],
&quot;answer&quot;: &quot;A&quot;
}
]

score = 0

print(&quot;================================&quot;)
print(&quot; PYTHON QUIZ GAME&quot;)
print(&quot;================================&quot;)

name = input(&quot;Enter your name: &quot;)
print(&quot;\nWelcome&quot;, name)
print(&quot;Total Questions:&quot;, len(questions))

for q in questions:

print(&quot;\n&quot; + q[&quot;question&quot;])

for option in q[&quot;options&quot;]:
print(option)

user_answer = input(&quot;Choose A/B/C/D : &quot;).upper()

if user_answer == q[&quot;answer&quot;]:
print(&quot; Correct&quot;)
score += 1
else:
print(&quot; Wrong&quot;)
print(&quot;Correct Answer:&quot;, q[&quot;answer&quot;])

print(&quot;\n================================&quot;)
print(&quot; SCORE BOARD&quot;)
print(&quot;================================&quot;)

print(&quot;Player:&quot;, name)
print(&quot;Correct Answers:&quot;, score)
print(&quot;Wrong Answers:&quot;, len(questions)-score)

percentage=(score/len(questions))*100

print(&quot;Score:&quot;, percentage,&quot;%&quot;)

if percentage &gt;= 80:
print(&quot; Excellent&quot;)
elif percentage &gt;= 50:
print(&quot; Good Job&quot;)
else:
print(&quot; Keep Practicing&quot;)

quiz()
