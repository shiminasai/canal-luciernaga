import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { AlertNewsComponent } from './alert-news.component';

describe('AlertNewsComponent', () => {
  let component: AlertNewsComponent;
  let fixture: ComponentFixture<AlertNewsComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ AlertNewsComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(AlertNewsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
