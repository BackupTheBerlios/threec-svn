<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Welcome to the Collaborative Coding Contest Hosting Page</title>
  </head>

  <body>
    
    Login<br/>
    Information must be entered because I don't have sessions enabled yet<br/>
    <form action="hostcontest" method="post">
      Name:<textarea name="user" rows="1" cols="15"></textarea><br/>
      Password:<input type="password" name="passwd" rows="1" cols="15" /><br/>
      <input type="submit" value="Login" /><br/>
    </form>
    
    <div>
      <font size="2">Powered by <a href="http://www.turbogears.org.nyud.net:8090/">Turbogears</a> and SQLite</font>
    </div>
  </body>
</html>
