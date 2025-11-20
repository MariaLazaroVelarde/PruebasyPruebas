package vallegrande.edu.pe.Pruebas.service.impl;

import vallegrande.edu.pe.Pruebas.model.Teacher;
import vallegrande.edu.pe.Pruebas.service.TeacherService;
import org.springframework.stereotype.Service;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Optional;
import java.util.concurrent.atomic.AtomicLong;

@Service
public class TeacherServiceImpl implements TeacherService {
    
    private final Map<Long, Teacher> teacherMap = new HashMap<>();
    private final AtomicLong idGenerator = new AtomicLong(1);
    
    public TeacherServiceImpl() {
        // Initialize with some mock data
        Teacher teacher1 = new Teacher(idGenerator.getAndIncrement(), "John", "Doe", "john.doe@school.edu", "Mathematics", 5);
        Teacher teacher2 = new Teacher(idGenerator.getAndIncrement(), "Jane", "Smith", "jane.smith@school.edu", "Physics", 8);
        Teacher teacher3 = new Teacher(idGenerator.getAndIncrement(), "Robert", "Johnson", "robert.johnson@school.edu", "Chemistry", 3);
        
        teacherMap.put(teacher1.getId(), teacher1);
        teacherMap.put(teacher2.getId(), teacher2);
        teacherMap.put(teacher3.getId(), teacher3);
    }
    
    @Override
    public List<Teacher> getAllTeachers() {
        return new ArrayList<>(teacherMap.values());
    }
    
    @Override
    public Optional<Teacher> getTeacherById(Long id) {
        return Optional.ofNullable(teacherMap.get(id));
    }
    
    @Override
    public Teacher saveTeacher(Teacher teacher) {
        // For new teachers (ID is null), assign a new ID
        if (teacher.getId() == null) {
            teacher.setId(idGenerator.getAndIncrement());
        }
        // For existing teachers, keep the existing ID
        teacherMap.put(teacher.getId(), teacher);
        return teacher;
    }
    
    @Override
    public void deleteTeacher(Long id) {
        teacherMap.remove(id);
    }
}