import { Component } from '@angular/core';
import { TopbarComponent } from '../topbar/topbar.component';


@Component({
  selector: 'app-home',
  standalone: true,
  imports: [TopbarComponent],
  templateUrl: './home.component.html',
  styleUrl: './home.component.scss'
})
export class HomeComponent {
  totalFrota = 332;
  veiculosRetidos = 8;
  frotaDisponivel = this.totalFrota - this.veiculosRetidos ;
}
