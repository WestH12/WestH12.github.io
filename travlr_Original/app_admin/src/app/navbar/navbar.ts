import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterLink, RouterLinkActive } from '@angular/router'; 
import { Authentication } from '../services/authentication'; 
import { RouterModule } from '@angular/router'; 

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './navbar.html',
  styleUrl: './navbar.css',
})
export class Navbar implements OnInit{
  constructor( 
    private authenticationService: Authentication,
    private router: Router
  ) { } 
 
  ngOnInit() { } 
   
  public isLoggedIn(): boolean { 
    return this.authenticationService.isLoggedIn(); 
  } 
 
  public onLogout(): void { 
    this.authenticationService.logout();
  } 
}
