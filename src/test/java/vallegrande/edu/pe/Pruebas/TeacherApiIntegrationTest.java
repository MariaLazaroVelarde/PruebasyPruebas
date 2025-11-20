package vallegrande.edu.pe.Pruebas;

import vallegrande.edu.pe.Pruebas.model.Teacher;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.MethodOrderer;
import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.TestMethodOrder;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.web.client.TestRestTemplate;
import org.springframework.boot.test.web.server.LocalServerPort;
import org.springframework.http.*;

import static org.junit.jupiter.api.Assertions.*;

@SpringBootTest(webEnvironment = SpringBootTest.WebEnvironment.RANDOM_PORT)
@TestMethodOrder(MethodOrderer.OrderAnnotation.class)
public class TeacherApiIntegrationTest {

    @LocalServerPort
    private int port;

    @Autowired
    private TestRestTemplate restTemplate;

    @Autowired
    private ObjectMapper objectMapper;

    private String createURLWithPort(String uri) {
        return "http://localhost:" + port + uri;
    }

    @Test
    public void shouldGetAllTeachers() {
        ResponseEntity<String> response = restTemplate.getForEntity(createURLWithPort("/api/teachers"), String.class);
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertTrue(response.getBody().contains("John"));
        assertTrue(response.getBody().contains("Doe"));
    }

    @Test
    public void shouldGetTeacherById() {
        ResponseEntity<Teacher> response = restTemplate.getForEntity(createURLWithPort("/api/teachers/1"), Teacher.class);
        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("John", response.getBody().getFirstName());
        assertEquals("Doe", response.getBody().getLastName());
    }

    @Test
    public void shouldReturnNotFoundForNonExistingTeacher() {
        ResponseEntity<String> response = restTemplate.getForEntity(createURLWithPort("/api/teachers/999"), String.class);
        assertEquals(HttpStatus.NOT_FOUND, response.getStatusCode());
    }

    @Test
    public void shouldCreateNewTeacher() throws Exception {
        Teacher teacher = new Teacher();
        teacher.setFirstName("Alice");
        teacher.setLastName("Brown");
        teacher.setEmail("alice.brown@school.edu");
        teacher.setSubject("Biology");
        teacher.setYearsOfExperience(4);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<String> entity = new HttpEntity<>(objectMapper.writeValueAsString(teacher), headers);

        ResponseEntity<Teacher> response = restTemplate.postForEntity(createURLWithPort("/api/teachers"), entity, Teacher.class);
        assertEquals(HttpStatus.CREATED, response.getStatusCode());
        assertNotNull(response.getBody());
        assertEquals("Alice", response.getBody().getFirstName());
        assertEquals("Biology", response.getBody().getSubject());
    }

    @Test
    public void shouldUpdateExistingTeacher() throws Exception {
        // First, verify the teacher exists
        ResponseEntity<String> getResponse = restTemplate.getForEntity(createURLWithPort("/api/teachers/1"), String.class);
        assertEquals(HttpStatus.OK, getResponse.getStatusCode());

        // Create a teacher object without ID for the update request
        String teacherJson = "{\"firstName\":\"John\",\"lastName\":\"Doe Updated\",\"email\":\"john.updated@school.edu\",\"subject\":\"Advanced Mathematics\",\"yearsOfExperience\":6}";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        HttpEntity<String> entity = new HttpEntity<>(teacherJson, headers);

        ResponseEntity<String> response = restTemplate.exchange(
                createURLWithPort("/api/teachers/1"),
                HttpMethod.PUT,
                entity,
                String.class
        );

        assertEquals(HttpStatus.OK, response.getStatusCode());
        assertTrue(response.getBody().contains("Doe Updated"));
        assertTrue(response.getBody().contains("Advanced Mathematics"));
    }

    @Test
    public void shouldDeleteTeacher() {
        // First, verify the teacher exists
        ResponseEntity<String> getResponse = restTemplate.getForEntity(createURLWithPort("/api/teachers/1"), String.class);
        assertEquals(HttpStatus.OK, getResponse.getStatusCode());

        ResponseEntity<String> response = restTemplate.exchange(
                createURLWithPort("/api/teachers/1"),
                HttpMethod.DELETE,
                null,
                String.class
        );

        assertEquals(HttpStatus.NO_CONTENT, response.getStatusCode());

        // Verify teacher is deleted
        ResponseEntity<String> verifyResponse = restTemplate.getForEntity(createURLWithPort("/api/teachers/1"), String.class);
        assertEquals(HttpStatus.NOT_FOUND, verifyResponse.getStatusCode());
    }
}