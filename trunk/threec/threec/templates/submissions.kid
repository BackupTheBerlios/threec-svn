<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
      py:extends="'master.kid'">

  <head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>View The Contest Log</title>
  </head>
  
  <body>
    <table>
      <tr align="center">
	<td>User Name</td><td>Problem</td><td>Result</td><td>Speed</td><td>Memory</td><td>Time</td><td>Code</td>
      </tr>
      <tr py:for="subm in submissions" align="center">
	<td>${subm.user.user}</td>
	<td>${subm.problem.problemName}</td>
	<td>${subm.response}</td>
	<td>${subm.speed}</td>
	<td>${subm.memory}</td>
	<td>${subm.time}</td>
	<td><a href="/viewcode?submissionId=${subm.id}">${subm.language}</a></td>
      </tr>
    </table>
  </body>
</html>
