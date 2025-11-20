package vallegrande.edu.pe.Pruebas.model;

import lombok.Data;
import lombok.NoArgsConstructor;
import lombok.AllArgsConstructor;

@Data
@NoArgsConstructor
@AllArgsConstructor
public class Teacher {
    private Long id;
    private String firstName;
    private String lastName;
    private String email;
    private String subject;
    private int yearsOfExperience;
}