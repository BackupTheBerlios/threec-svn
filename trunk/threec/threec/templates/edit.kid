<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Welcome to TurboGears</title>
</head>

<body>

  <div style="float:right; width:10em">Editting<span py:replace="pagename">page name goes here</span><br/>
    <a href="/">FrontPage</a></div>
  <form action="save" method="post"> 
    <input type="hidden" name="pagename" value="${pagename}"/>
    <textarea name="data" py:content="data" rows="10" cols="60">page text goes here</textarea> 
    <input type="submit" name="submit" value="Save"/> 
  </form> 
  
</body>
</html>
