package vallegrande.edu.pe.Pruebas;

import vallegrande.edu.pe.Pruebas.model.Teacher;
import vallegrande.edu.pe.Pruebas.service.TeacherService;
import vallegrande.edu.pe.Pruebas.service.impl.TeacherServiceImpl;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.List;
import java.util.Optional;

import static org.junit.jupiter.api.Assertions.*;

public class TeacherServiceTest {

    private TeacherService teacherService;

    @BeforeEach
    public void setUp() {
        teacherService = new TeacherServiceImpl();
    }

    @Test
    public void shouldReturnAllTeachers() {
        List<Teacher> teachers = teacherService.getAllTeachers();
        assertEquals(3, teachers.size());
    }

    @Test
    public void shouldReturnTeacherById() {
        Optional<Teacher> teacher = teacherService.getTeacherById(1L);
        assertTrue(teacher.isPresent());
        assertEquals("John", teacher.get().getFirstName());
        assertEquals("Doe", teacher.get().getLastName());
    }

    @Test
    public void shouldReturnEmptyForNonExistingTeacher() {
        Optional<Teacher> teacher = teacherService.getTeacherById(999L);
        assertFalse(teacher.isPresent());
    }

    @Test
    public void shouldSaveNewTeacher() {
        Teacher newTeacher = new Teacher();
        newTeacher.setFirstName("Alice");
        newTeacher.setLastName("Brown");
        newTeacher.setEmail("alice.brown@school.edu");
        newTeacher.setSubject("Biology");
        newTeacher.setYearsOfExperience(4);

        Teacher savedTeacher = teacherService.saveTeacher(newTeacher);
        assertNotNull(savedTeacher.getId());
        assertEquals("Alice", savedTeacher.getFirstName());
    }

    @Test
    public void shouldUpdateExistingTeacher() {
        // First, get an existing teacher
        Optional<Teacher> existingTeacher = teacherService.getTeacherById(1L);
        assertTrue(existingTeacher.isPresent());

        // Update the teacher
        Teacher updatedTeacher = new Teacher();
        updatedTeacher.setId(1L); // Set the ID to match the existing teacher
        updatedTeacher.setFirstName("John");
        updatedTeacher.setLastName("Doe Updated");
        updatedTeacher.setEmail("john.updated@school.edu");
        updatedTeacher.setSubject("Advanced Mathematics");
        updatedTeacher.setYearsOfExperience(6);

        Teacher savedTeacher = teacherService.saveTeacher(updatedTeacher);
        assertEquals(1L, savedTeacher.getId());
        assertEquals("Doe Updated", savedTeacher.getLastName());
        assertEquals("Advanced Mathematics", savedTeacher.getSubject());
    }

    @Test
    public void shouldDeleteTeacher() {
        // First, verify the teacher exists
        Optional<Teacher> existingTeacher = teacherService.getTeacherById(1L);
        assertTrue(existingTeacher.isPresent());

        // Delete the teacher
        teacherService.deleteTeacher(1L);

        // Verify the teacher is deleted
        Optional<Teacher> deletedTeacher = teacherService.getTeacherById(1L);
        assertFalse(deletedTeacher.isPresent());
    }
}