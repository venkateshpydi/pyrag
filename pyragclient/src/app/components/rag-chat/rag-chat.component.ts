import {
  Component
} from '@angular/core';

import {
  CommonModule
} from '@angular/common';

import {
  FormsModule
} from '@angular/forms';

import {
  RagService
} from '../../services/rag.service';

import {
  ChatMessage
} from '../../models/chat-message';

@Component({
  selector: 'app-rag-chat',
  standalone: true,
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './rag-chat.component.html',
  styleUrls: ['./rag-chat.component.css']
})
export class RagChatComponent {

  question = '';

  loading = false;

  messages: ChatMessage[] = [];

  constructor(
    private ragService: RagService
  ) {}

  askQuestion(): void {

    if (!this.question.trim()) {
      return;
    }

    const userQuestion = this.question;

    this.messages.push({
      text: userQuestion,
      sender: 'user',
      timestamp: new Date()
    });

    this.question = '';

    this.loading = true;

    this.ragService
      .askQuestion(userQuestion)
      .subscribe({
        next: response => {

          this.messages.push({
            text: response.answer,
            sender: 'bot',
            timestamp: new Date()
          });
         // console.log(this.messages);
          this.loading = false;
        },
        error: error => {

          this.messages.push({
            text:
              'Sorry, I encountered an error.',
            sender: 'bot',
            timestamp: new Date()
          });

          this.loading = false;

          console.error(error);
        }
      });
  }
}