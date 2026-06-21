import { Component, OnInit } from '@angular/core';import { CommonModule } from '@angular/common'; 
import { Router } from '@angular/router'; 
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from "@angular/forms"; 
import { TripData } from '../services/trip-data'; 
import { Trip } from '../models/trip'; 

@Component({
  selector: 'app-delete-trip',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './delete-trip.html',
  styleUrl: './delete-trip.css',
})
export class DeleteTrip implements OnInit {
  
  trip!: Trip;
  message : string ='';

  constructor(
    private router: Router,
    private tripDataService: TripData
  ){}

  ngOnInit(): void {
    
    let tripCode = localStorage.getItem("tripCode");
    if(!tripCode){
      alert("Something wrong, couldn't find where I stashed tripCode!");
      this.router.navigate(['']);
      return;
    }

    this.tripDataService.deleteTrip(tripCode)
      .subscribe({
        next: (value: any) => {
          this.trip = value;

          if(!value){
            this.message = "No trip deleted!";
            console.log(this.message);
            this.router.navigate(['']);
          } else {
            this.message = 'Trip ' + tripCode + ' deleted!';
            console.log(this.message);
            this.router.navigate(['']);
          }
          
        },
        error: (error: any) => {
          console.log('Error: ' + error);
        }
      })



  }

}
