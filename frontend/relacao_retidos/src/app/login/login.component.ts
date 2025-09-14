import { Component } from '@angular/core';
import { MatInputModule } from '@angular/material/input';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { Router } from '@angular/router';
import { FormGroup, FormControl, ReactiveFormsModule, FormsModule, Validators } from '@angular/forms';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [
    FormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule,
    ReactiveFormsModule
  ],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss'
})
export class LoginComponent {
  // eslint-disable-next-line @angular-eslint/prefer-inject
  constructor(private router: Router) {}
  esconder = true;
  dadosUsuario = new FormGroup({
    usuario: new FormControl(null, [Validators.required, Validators.email]),
    senha: new FormControl(null, Validators.required),
  });

  esconderSenha(): void {
    this.esconder = !this.esconder;
  }

  entrar(): void {
    console.log('Clicou pra entrar');
    console.log("formulario ", this.dadosUsuario);
    console.log("Usuario ->>> ", this.dadosUsuario.value.usuario);
    console.log("Senha ->>> ", this.dadosUsuario.value.senha);

    if (this.dadosUsuario.invalid) {
      console.log("Preencha os dados corretamente!");
    } else {
      this.router.navigate(['/inicio']);
    }
  }
}
