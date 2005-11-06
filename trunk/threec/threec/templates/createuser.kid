<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">
  <head>
    <title>Creating Your Account</title>
  </head>
  <body>
    <form action="createaccount" method="post">
      Desired Username:<textarea name="username" rows="1" cols="15"></textarea><br/>
      Desired Password:<input name="passwd" type="password" rows="1" cols="15"/><br/>
      Confirm Password:<input name="passwdchk" type="password" rows="1" cols="15"/><br/>
      Email:<textarea name="email" rows="1" cols="15"></textarea>
      <br/>(Only used for password resets)<br/>
      <input type="submit" value="Create" />
    </form>
  </body>
</html>
