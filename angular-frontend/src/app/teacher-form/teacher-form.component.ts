import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Teacher } from '../models/teacher.model';
import { TeacherService } from '../services/teacher.service';

@Component({
  selector: 'app-teacher-form',
  templateUrl: './teacher-form.component.html',
  styleUrl: './teacher-form.component.scss'
})
export class TeacherFormComponent implements OnInit {
  teacherForm: FormGroup;
  isEditing = false;
  currentTeacherId: number | null = null;

  @Output() teacherSaved = new EventEmitter<void>();

  constructor(
    private fb: FormBuilder,
    private teacherService: TeacherService
  ) {
    this.teacherForm = this.fb.group({
      firstName: ['', Validators.required],
      lastName: ['', Validators.required],
      email: ['', [Validators.required, Validators.email]],
      subject: ['', Validators.required],
      yearsOfExperience: [0, [Validators.required, Validators.min(0)]]
    });
  }

  ngOnInit(): void {
  }

  onSubmit(): void {
    if (this.teacherForm.valid) {
      const teacher: Teacher = this.teacherForm.value;
      
      if (this.isEditing && this.currentTeacherId) {
        this.teacherService.updateTeacher(this.currentTeacherId, teacher).subscribe({
          next: (updatedTeacher) => {
            console.log('Teacher updated successfully', updatedTeacher);
            this.resetForm();
            this.teacherSaved.emit();
          },
          error: (error) => {
            console.error('Error updating teacher', error);
          }
        });
      } else {
        this.teacherService.createTeacher(teacher).subscribe({
          next: (newTeacher) => {
            console.log('Teacher created successfully', newTeacher);
            this.resetForm();
            this.teacherSaved.emit();
          },
          error: (error) => {
            console.error('Error creating teacher', error);
          }
        });
      }
    }
  }

  editTeacher(teacher: Teacher): void {
    this.teacherForm.patchValue(teacher);
    this.isEditing = true;
    this.currentTeacherId = teacher.id || null;
  }

  resetForm(): void {
    this.teacherForm.reset({ yearsOfExperience: 0 });
    this.isEditing = false;
    this.currentTeacherId = null;
  }
}