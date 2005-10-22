<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Member List</title>
  </head>

  <body>
    <p>You searched for <span py:replace="user"> username </span></p>
    <p> 
      Here are <span py:replace="user">username</span>'s stats as a <span py:replace="type"> coder/problemsetter </span>
    </p>
    <div>
      <font size="2">Powered by <a href="http://www.turbogears.org.nyud.net:8090/">Turbogears</a> and SQLite</font>
    </div>
  </body>
</html>
