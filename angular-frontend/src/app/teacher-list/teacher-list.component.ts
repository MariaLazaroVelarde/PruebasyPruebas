import { Component, OnInit, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Teacher } from '../models/teacher.model';
import { TeacherService } from '../services/teacher.service';

@Component({
  selector: 'app-teacher-list',
  templateUrl: './teacher-list.component.html',
  styleUrl: './teacher-list.component.scss'
})
export class TeacherListComponent implements OnInit {
  teachers: Teacher[] = [];
  loading = false;

  @Output() editTeacher = new EventEmitter<Teacher>();

  constructor(private teacherService: TeacherService) { }

  ngOnInit(): void {
    this.loadTeachers();
  }

  loadTeachers(): void {
    this.loading = true;
    this.teacherService.getAllTeachers().subscribe({
      next: (data) => {
        this.teachers = data;
        this.loading = false;
      },
      error: (error) => {
        console.error('Error loading teachers', error);
        this.loading = false;
      }
    });
  }

  deleteTeacher(id: number | undefined): void {
    if (id === undefined) return;
    
    if (confirm('Are you sure you want to delete this teacher?')) {
      this.teacherService.deleteTeacher(id).subscribe({
        next: () => {
          this.loadTeachers(); // Reload the list after deletion
        },
        error: (error) => {
          console.error('Error deleting teacher', error);
        }
      });
    }
  }

  onEditTeacher(teacher: Teacher): void {
    this.editTeacher.emit(teacher);
  }
}