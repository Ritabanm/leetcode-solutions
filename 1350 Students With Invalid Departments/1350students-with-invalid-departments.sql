select students.id, students.name
from departments right join students on departments.id = students.department_id
where departments.id is null