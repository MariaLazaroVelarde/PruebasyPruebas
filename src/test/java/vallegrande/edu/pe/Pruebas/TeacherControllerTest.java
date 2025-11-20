package vallegrande.edu.pe.Pruebas;

import vallegrande.edu.pe.Pruebas.model.Teacher;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.http.MediaType;
import org.springframework.test.annotation.DirtiesContext;
import org.springframework.test.web.servlet.MockMvc;

import static org.hamcrest.Matchers.hasSize;
import static org.hamcrest.Matchers.is;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.*;

@SpringBootTest
@AutoConfigureMockMvc
@DirtiesContext(classMode = DirtiesContext.ClassMode.AFTER_EACH_TEST_METHOD)
public class TeacherControllerTest {

    @Autowired
    private MockMvc mockMvc;

    @Autowired
    private ObjectMapper objectMapper;

    @Test
    public void shouldGetAllTeachers() throws Exception {
        mockMvc.perform(get("/api/teachers"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$", hasSize(3)));
    }

    @Test
    public void shouldGetTeacherById() throws Exception {
        mockMvc.perform(get("/api/teachers/1"))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.firstName", is("John")))
                .andExpect(jsonPath("$.lastName", is("Doe")));
    }

    @Test
    public void shouldReturnNotFoundForNonExistingTeacher() throws Exception {
        mockMvc.perform(get("/api/teachers/999"))
                .andExpect(status().isNotFound());
    }

    @Test
    public void shouldCreateNewTeacher() throws Exception {
        Teacher teacher = new Teacher();
        teacher.setFirstName("Alice");
        teacher.setLastName("Brown");
        teacher.setEmail("alice.brown@school.edu");
        teacher.setSubject("Biology");
        teacher.setYearsOfExperience(4);

        mockMvc.perform(post("/api/teachers")
                .contentType(MediaType.APPLICATION_JSON)
                .content(objectMapper.writeValueAsString(teacher)))
                .andExpect(status().isCreated())
                .andExpect(jsonPath("$.firstName", is("Alice")))
                .andExpect(jsonPath("$.subject", is("Biology")));
    }

    @Test
    public void shouldUpdateExistingTeacher() throws Exception {
        // Create a teacher object without ID for the update request
        // The ID will be taken from the path variable
        String teacherJson = "{\"firstName\":\"John\",\"lastName\":\"Doe Updated\",\"email\":\"john.updated@school.edu\",\"subject\":\"Advanced Mathematics\",\"yearsOfExperience\":6}";

        mockMvc.perform(put("/api/teachers/1")
                .contentType(MediaType.APPLICATION_JSON)
                .content(teacherJson))
                .andExpect(status().isOk())
                .andExpect(jsonPath("$.lastName", is("Doe Updated")))
                .andExpect(jsonPath("$.subject", is("Advanced Mathematics")));
    }

    @Test
    public void shouldDeleteTeacher() throws Exception {
        mockMvc.perform(delete("/api/teachers/1"))
                .andExpect(status().isNoContent());
                
        // Verify teacher is deleted
        mockMvc.perform(get("/api/teachers/1"))
                .andExpect(status().isNotFound());
    }
}