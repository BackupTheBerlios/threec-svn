<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">

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
    
    <br/>
    <a href="/contests">All Competitions</a><br/>
    <a href="/upcomingcontests">Upcoming Competitions</a><br/>


    Manage your Competitions:<br/>
    <form action="hostcontests" method="post">
      Name:<textarea name="user" rows="1" cols="15"></textarea><br/>
      Password:<input type="password" name="passwd" rows="1" cols="15" /><br/>
      <input type="submit" value="Login" /><br/>
    </form>
      
    <br />
    Search for a User:<br/>
    <form action="searchusers" method="post">
      <textarea name="userName" rows="1" cols="15"></textarea><br/>      
      <input type="submit" value="Search" /><br/>
    </form><br/>
    
    <div>
      <font size="2">Powered by <a href="http://www.turbogears.org.nyud.net:8090/">Turbogears</a> and SQLite</font>
    </div>
  </body>
</html>
