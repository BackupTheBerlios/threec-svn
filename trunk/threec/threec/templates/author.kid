<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
      py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Problems made by ${author}</title>
  </head>
  
  <span>
    All problems by ${author}:
  </span>

  <body>
    <ul>
      <li py:for="problem in problems">
	<a href="${problem[1]}">${problem[0]}</a>
      </li>
    </ul>
  </body>
</html>
