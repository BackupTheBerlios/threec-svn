<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
      py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>All Contests</title>
  </head>
  
  <body>
    <table>
      <tr align="center">
	<td>Name</td><td>Start</td><td>End</td><td>Created By</td><td py:if="showProblemSetLink">Problem Set</td>
      </tr>
      <tr py:for="contest in contests" align="center">
	<td py:content="contest[0]">Name</td>
	<td py:content="contest[1]">Start</td>
	<td py:content="contest[2]">End</td>
	<td py:content="contest[3]"><a href="/searchUsers?userName=${contest[3]}">Created By</a></td>
	<td py:if="showProblemSetLink"><a href="${contest[4]}">View Problems</a></td>
      </tr>
    </table>
  </body>
</html>
