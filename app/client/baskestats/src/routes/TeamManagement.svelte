<script>
  import { onMount } from 'svelte';
  
  // Initialize teams as an empty array
  let teams = [];

  // Fetch teams data from the backend
async function fetchTeams() {
  try {
    const response = await fetch('http://127.0.0.1:5003/teams'); // Replace with your API endpoint
    if (response.ok) {
      const teamData = await response.json();
      
      // Assuming the structure is [[team_id, team_name, team_city, team_wins, team_losses], ...]
      teams = teamData.map(team => ({
        id: team[0],
        name: team[1],
        city: team[2],
        wins: team[3],
        losses: team[4],
      }));

      // teams array assumed to be an array of objects with specific properties for each team
    } else {
      console.error('Failed to fetch teams:', response.status);
      // Handle error
    }
  } catch (error) {
    console.error('Error fetching teams:', error);
    // Handle error
  }
}

  // Fetch teams data on component mount
  onMount(fetchTeams);
  function handleClick(event) {
    // Handle the click event here
    console.log('Button clicked!');
  }
</script>

<h1>Team Management</h1>

<div>
<button on:click={handleClick}>Create New Team</button>
</div>
<div>
<!-- Table w/ available teams -->
<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>City</th>
      <th>Wins</th>
      <th>Losses</th>
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
</div>