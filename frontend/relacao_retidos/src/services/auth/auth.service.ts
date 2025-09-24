import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private http: HttpClient
  ) { }

  this.http.get<Config>('/api/config', {observe: 'response'}).subscribe(res => {
    console.log('Response status:', res.status);
    console.log('Body:', res.body);
  });
}
