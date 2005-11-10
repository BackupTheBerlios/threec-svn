<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Member List</title>
  </head>

  <body>
    <p>User information for <span py:replace="user"> username </span></p>

    <table>
      <tr align="center">
	<td>Problem</td><td>Code</td>
      </tr>
      <tr py:for="subm in submissions" align="center">
	<td><a href="${subm[1]}">${subm[0]}</a></td>
	<td><a href="${subm[2]}">View Code</a></td>
      </tr>
    </table>
  </body>
</html>
