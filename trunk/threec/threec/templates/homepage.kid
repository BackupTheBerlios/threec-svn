<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
      py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Welcome to the Collaborative Coding Contest Homepage</title>
  </head>

  <body>
    
    <p>New to CCubed? Create an Account!</p>
    <form action="createuser" method="post">
      <input type="submit" value="Create" /><br/>
    </form>
    
    Login<br/>
    <form action="login" method="post">
      Name:<textarea name="user" rows="1" cols="15"></textarea><br/>
      Password:<input type="password" name="passwd" rows="1" cols="15" /><br/>
      <input type="submit" value="Login" /><br/>
    </form>
    
    <a href="/RecentMatches">Recent Contests</a><br/>

    <br/>
    <a href="/calender">Upcoming Competitions</a><br/>
    <a href="/host">Manage your Competitions</a><br/>

    <br />
    Search for a User:<br/>
    <form action="searchuser" method="post">
      <textarea name="user" rows="1" cols="15"></textarea><br/>      
      <input type="radio" name="type" value="coder" checked="true">As a Coder</input>
      <input type="submit" value="Search" /><br/>
      <input type="radio" name="type" value="setter">As a Problem Setter</input>
    </form><br/>
    
    <div>
      <font size="2">Powered by <a href="http://www.turbogears.org.nyud.net:8090/">Turbogears</a> and SQLite</font>
    </div>
  </body>
</html>
