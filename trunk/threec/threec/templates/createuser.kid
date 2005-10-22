<html>
  <head>
    <title>Creating Your Account</title>
  </head>
  <body>
    <span>
      Came here in error? Log in from here.
      <form action="login" method="post">
	Name:<textarea name="user" rows="1" cols="15"></textarea><br/>
	Password:<input type="password" name="passwd" rows="1" cols="15" /><br/>
	<input type="submit" value="Login" /><br/>
      </form>
    </span>
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
