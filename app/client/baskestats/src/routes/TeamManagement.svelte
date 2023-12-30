<script>
  import { onMount } from 'svelte';
  
  // Initialize teams as an empty array
  let teams = [];

  // Fetch teams data from the backend
  async function fetchTeams() {
    try {
      const response = await fetch('http://127.0.0.1:5003/teams'); // Replace with your API endpoint for fetching teams
      if (response.ok) {
        teams = await response.json();
      } else {
        console.error('Failed to fetch teams:', response.status);
        // Handle error, show error message, etc.
      }
    } catch (error) {
      console.error('Error fetching teams:', error);
      // Handle error, show error message, etc.
    }
  }

  // Fetch teams data on component mount
  onMount(fetchTeams);
</script>

<h1>Team Management</h1>

<button>Create New Team</button>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <!-- Add more table headers if needed -->
    </tr>
  </thead>
  <tbody>
    {#each teams as team}
      <tr>
        <td>{team.id}</td>
        <td>{team.name}</td>
        <td>{team.city}</td>
        <td>{team.wins}</td>
        <td>{team.losses}</td>
        <!-- Render more table cells with team details -->
      </tr>
    {/each}
  </tbody>
</table>