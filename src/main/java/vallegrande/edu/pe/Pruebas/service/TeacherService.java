package vallegrande.edu.pe.Pruebas.service;

import vallegrande.edu.pe.Pruebas.model.Teacher;

import java.util.List;
import java.util.Optional;

public interface TeacherService {
    List<Teacher> getAllTeachers();
    Optional<Teacher> getTeacherById(Long id);
    Teacher saveTeacher(Teacher teacher);
    void deleteTeacher(Long id);
}