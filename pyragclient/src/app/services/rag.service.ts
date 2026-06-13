import { Injectable } from '@angular/core';

import {
  HttpClient
} from '@angular/common/http';

import {
  Observable
} from 'rxjs';

import {
  RagRequest
} from '../models/rag-request';

import {
  RagResponse
} from '../models/rag-response';

import {
  environment
} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class RagService {

  private readonly API_URL =
    `${environment.apiUrl}/api/v1/rag`;

  constructor(
    private http: HttpClient
  ) {}

  askQuestion(
    question: string
  ): Observable<RagResponse> {

    const request: RagRequest = {
      question
    };

    return this.http.post<RagResponse>(
      `${this.API_URL}/ask`,
      request
    );
  }
}