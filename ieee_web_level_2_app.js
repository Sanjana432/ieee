// _Level 2 - Interactive Page Clone with API_

// Fetch data from a mock API (using JSONPlaceholder for this example)
fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => response.json())
  .then(data => {
    data.slice(0, 6).forEach(idea => {
      const card = document.createElement('div');
      card.classList.add('card');
      card.innerHTML = `
        <img src="https://via.placeholder.com/300x200" alt="Idea Image" loading="lazy">
        <div class="card-content">
          <h3>${idea.title}</h3>
          <p>${idea.body}</p>
        </div>
      `;
      document.querySelector('.idea-cards').appendChild(card);
    });
  })
  .catch(error => console.error('Error fetching data:', error));
