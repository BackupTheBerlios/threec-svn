<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://purl.org/kid/ns#"
    py:extends="'master.kid'">

<head>
    <meta content="text/html; charset=UTF-8" http-equiv="content-type" />
    <title>Edit A Contest</title>
</head>

<?python
   import datetime
   year = int(datetime.datetime.now().year)
?>

<body>

  <form action="savecontest" method="post"> 
    Name:<textarea rows="1" name="name">${name}</textarea><br />
    Start:
    <select name="syear">
      <option py:for="x in range(2)" py:attrs="dict(value=x+year,selected=(start.year==(x+year) and 'selected' or None))">${x+year}</option>
    </select>
    <select name="smonth" selected="11">
      <option py:for="x in range(12)" py:attrs="dict(value=x+1,selected=(start.month==(x+1) and 'selected' or None))">${x+1}</option>
    </select>
    <select name="sday">
      <option py:for="x in range(30)" py:attrs="dict(value=x+1,selected=(start.day==(x+1) and 'selected' or None))">${x+1}</option>
    </select>
    <select name="shour">
      <option py:for="x in range(24)" py:attrs="dict(value=x,selected=(start.hour==(x) and 'selected' or None))">${x}</option>
    </select>
    <select name="smin">
      <option py:for="x in range(60)" py:attrs="dict(value=x,selected=(start.minute==(x) and 'selected' or None))">${x}</option>
    </select>

    <br />End:
    <select name="eyear">
      <option py:for="x in range(2)" py:attrs="dict(value=x+year,selected=(end.year==(x+year) and 'selected' or None))">${x+year}</option>
    </select>
    <select name="emonth">
      <option py:for="x in range(12)" py:attrs="dict(value=x+1,selected=(end.month==(x+1) and 'selected' or None))">${x+1}</option>
    </select>
    <select name="eday">
      <option py:for="x in range(30)" py:attrs="dict(value=x+1,selected=(end.day==(x+1) and 'selected' or None))">${x+1}</option>
    </select>
    <select name="ehour">
      <option py:for="x in range(24)" py:attrs="dict(value=x,selected=(end.hour==(x) and 'selected' or None))">${x}</option>
    </select>
    <select name="emin">
      <option py:for="x in range(60)" py:attrs="dict(value=x,selected=(end.minute==(x) and 'selected' or None))">${x}</option>
    </select>

    <input type="hidden" name="userId" value="${userId}" />
    <input type="hidden" name="contestId" value="${contestId}" />
    <br /><input type="submit" value="Save"/> 
  </form>
  
  <table>
    <tr>
      <td>Problem</td><td>Remove</td>
    </tr>
    <hr />
    <tr py:for="prob in problemset">
      <td><a href="${prob.problemUrl}">${prob.problemName}</a></td>
      <td><a href="/editcontest?problemId=${prob.id}&amp;userId=${userId}&amp;contestId=${contestId}">Edit</a></td>
      <td><a href="/remove?problemId=${prob.id}&amp;userId=${userId}&amp;contestId=${contestId}">Remove</a></td>
    </tr>
  </table>
  
  <form action="addproblem" method="post">
    Name:<textarea rows="1" name="name">${pname}</textarea><br />
    Author:<textarea rows="1" name="author">${pauthor}</textarea><br />
    Statement:<textarea rows="1" name="stmt">${pstmt}</textarea><br />
    Time Limit:<textarea rows="1" name="time">${ptime}</textarea><br />
    Memory Limit:<textarea rows="1" name="memory">${pmem}</textarea><br />
    Correctness:<textarea rows="1" name="correct">${pcor}</textarea><br />
    <input type="hidden" name="problemId" value="${problemId}" />
    <input type="hidden" name="userId" value="${userId}" />
    <input type="hidden" name="contestId" value="${contestId}" />
    <input type="submit" value="Add Problem to Contest"/>
  </form>

</body>
</html>
