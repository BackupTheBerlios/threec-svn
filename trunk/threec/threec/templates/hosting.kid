<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#" py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Manage your contests</title>
  </head>
  
  <body>


    <table>
      <tr align="center">
	<td>Contest Name</td><td>Contest Start</td><td>Contest End</td>
      </tr>
      <tr>
	<td align="center">Prior Contests</td>
      </tr>
      <tr py:for="contest in prior" align="center">
	<td><a href="/submissions?contestId=${contest.id}">${contest.name}</a></td>
	<td>{$contest.start}</td><td>{$contest.end}</td>
      </tr>
      <tr><td align="center">Upcoming Contest</td></tr>
      <tr py:for="contest in upcoming" align="center">
	<td><a href="/editcontest?contestId=${contest.id}&amp;userId=${userId}">${contest.name}</a></td>
	<td>{$contest.start}</td><td>{$contest.end}</td>
      </tr>
    </table>

    <a href="/editcontest?contestId=0&amp;userId=${userId}">Add a new contest</a>

  </body>
</html>
