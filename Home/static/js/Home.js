if (localStorage.getItem("Token") )
{
    
}
else
{
    LogOut();
}
function SearchByEnter()
{
   if(event.keyCode==13)
   {
     GetStudentByStudentName();
   }
}
function LogOut()
{
    localStorage.removeItem('Token');
    window.location="/Login";
    
}
function GetStudentByStudentName(){
    var name=document.getElementById('SearchByStudenName').value;
    const xhttp = new XMLHttpRequest();
    xhttp.onload = function() 
    {
        if(xhttp.status==403)
        {
            localStorage.removeItem('Token');
            window.location='/Login';
        }
        else if(xhttp.status==404)
        {
            alert("Không có sinh viên nào")
        }
        var studentsJsons=xhttp.responseText;
        var students= JSON.parse(studentsJsons);
        if(xhttp.status==200)
        {
            var studentsHtml = '<thead><tr><th>Tên Học Sinh</th><th>Mã Sinh Viên</th><th>Điểm</th><tr></thead> <tbody>';
            for (var i in students)
            {
                studentsHtml+='<tr><td>'+students[i].StudentName+'</td><td>'+students[i].StudentCode+'</td><td>'+String(students[i].Scores)+'</td></tr>';
            }
            studentsHtml+='</tbody>';
            document.getElementById("table__Studentlist").innerHTML=studentsHtml;
        }
    }            
    xhttp.open("GET", "/Student/"+name,false);
    token = localStorage.getItem("Token");
    authorization ='Bearer '+token
    xhttp.setRequestHeader("Authorization",authorization);
    xhttp.send();
}

