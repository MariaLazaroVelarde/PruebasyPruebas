import { Component, ViewChild } from '@angular/core';
import { Teacher } from './models/teacher.model';
import { TeacherFormComponent } from './teacher-form/teacher-form.component';
import { TeacherListComponent } from './teacher-list/teacher-list.component';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'teacher-management-frontend';
  
  @ViewChild(TeacherFormComponent) teacherForm!: TeacherFormComponent;
  @ViewChild(TeacherListComponent) teacherList!: TeacherListComponent;

  onEditTeacher(teacher: Teacher): void {
    if (this.teacherForm) {
      this.teacherForm.editTeacher(teacher);
    }
  }

  onTeacherSaved(): void {
    if (this.teacherList) {
      this.teacherList.loadTeachers();
    }
  }
}