const request = require('supertest');
const app = require('../app');

describe('Teste de integração', () => {
  it('Deve exibir a lista de notícias na página principal', async () => {
    const response = await request(app).get('/');
    expect(response.statusCode).toBe(200);
    expect(response.text).toContain('Notícias de tecnologia');
  });

  it('Deve exibir uma notícia específica ao clicar em um título', async () => {
    const response = await request(app).get('/noticias/1');
    expect(response.statusCode).toBe(200);
    expect(response.text).toContain('Detalhes da notícia');
  });
});
