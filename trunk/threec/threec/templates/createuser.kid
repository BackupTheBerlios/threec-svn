<html xmlns:py="http://purl.org/kid/ns#">

<?python
try:
   if message:
      pass
except NameError:
   message = []
print 'ok all'
?>
  <head>
    <title>Creating Your Account</title>
  </head>
  <body>
    <span py:for="msg in message">
      <p py:content="msg">Message to be displayed</p>
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
