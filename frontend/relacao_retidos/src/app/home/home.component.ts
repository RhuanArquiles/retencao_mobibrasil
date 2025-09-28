import { Component } from '@angular/core';
import { TopbarComponent } from '../topbar/topbar.component';
import { RouterLink } from "@angular/router";
import { LoginComponent } from '../login/login.component';

@Component({
  selector: 'app-home',
  standalone: true,
  imports: [TopbarComponent, RouterLink, LoginComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  totalFrota = 332;
  veiculosRetidos = 8;
  frotaDisponivel = this.totalFrota - this.veiculosRetidos ;
}
