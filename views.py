from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registerpage(request):
    data = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>register page</title>
    </head>
    <body bgcolor="lavender">
    <br>
    <br>
    <form>
        <label> Firstname </label>
        <input type="text" name="Firstname" size="15"/> <br><br>
        <label> Middlename </label>
        <input type="text" name="middlename" size="15"/> <br><br>
        <label> Lastname </label>
        <input type="text" name="lastname" size="15"/> <br><br>


        <label>
            Course:
        </label>
        <select>
            <option value="Course">Course</option>
            <option value="BCA">BCA</option>
            <option value="BBA">BBA</option>
            <option value="B.Tech">B.Tech</option>
            <option value="MBA">MBA</option>
            <option value="MCA">MCA</option>
            <option value="M.Tech">M.Tech</option>
        </select>

        <br>
        <br>
        <label>
            Gender:
        </label><br>
        <input type="radio" name="male"/> Male <br>
        <input type="radio" name="female"/> Female <br>
        <input type="radio" name="other"/> other
        <br>
        <br>

        <label>
            Phone:
        </label>
        <input type="text" name="country code" value="+91"size="2"/>
        <input type="text" name="Phone" size="10"/> <br> </br>
        Address:
        <br>
        <textarea cols="80" rows="5" value="address">
        </textarea>
        <br> <br>
        Email:
        <input type="email" id="email" name="email"/> <br>
        <br><br>
        Password:
        <input type="password" id="pass" name="pass"> <br>
        <br><br> 
        Re-type password:
        <input type="Password" id="repass" name="repass"> <br><br> 
        <input type="button" value="Submit">    
    </form>
    </body>
    </html>
    """
    return HttpResponse(data)


