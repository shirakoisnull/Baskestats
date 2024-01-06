<script>
  import { navigate } from "svelte-routing";
  import { onMount } from "svelte";
  import { fetchTeams } from "../api.js";

  let teams = []; // Fetch and populate this array with available teams data
  let selectedTeams = [];
  let selectedTeamId = null;

  // Fetch available teams when the component mounts
  onMount(async () => {
    teams = await fetchTeams();
    console.log(teams);
  });



function addTeam(selectedTeam) {
    if (!selectedTeams.some(team => team[0] === selectedTeam[0])) {
      selectedTeams = [...selectedTeams, selectedTeam];
    }
  }

  function removeTeam(index) {
    selectedTeams = selectedTeams.filter((_, i) => i !== index);
  }

  async function submitSelection() {
    const selectedTeamIds = selectedTeams.map(team => team[0]); // Assuming team[0] holds the team ID
    console.log('Selected Teams:', selectedTeamIds);

    fetch('http://127.0.0.1:5005/championships/draw', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ teams: selectedTeamIds })
    }).then(response => {
        if (response.ok) {
            console.log('Teams submitted successfully!');
            navigate("/champ"); 
        } else {
            console.error('Failed to submit teams:', response.statusText);
        }
    }).catch(error => {
        console.error('Error submitting teams:', error);
    });
  }
</script>

<h1>Draw Championship</h1>
<div class="container">
  <div class="left-section">
    <div class="dropdown-wrapper">
      <select bind:value={selectedTeamId}>
        {#each teams as team}
          <option value={team[0]}>{team[1]}</option>
        {/each}
      </select>
      <button class="add-btn" on:click={() => addTeam(teams.find(t => t[0] === parseInt(selectedTeamId)))}>➕</button>
    </div>
    <button class="submit-btn" on:click={submitSelection}>Submit</button>
  </div>

  <div class="right-section">
    <div class="selected-teams">
      <table>
        <thead>
          <tr>
            <!-- <th>ID</th> -->
            <th>Name</th>
            <!-- Add other headers based on team data structure -->
            <th>Action</th>
          </tr>
        </thead>
        <tbody>
          {#each selectedTeams as team, index}
            <tr>
              <!-- <td>{team[0]}</td> -->
              <td>{team[1]}</td>
              <!-- Display other team data based on its structure -->
              <td><button class="remove-btn" on:click={() => removeTeam(index)}>Remove</button></td>
            </tr>
          {/each}
        </tbody>
      </table>
    </div>
  </div>
</div>

<button class="back-button" on:click={() => navigate("/champ")}>Go Back</button>
<style>
  .container {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
  }

  .left-section {
    width: 40%;
  }

  .right-section {
    width: 60%;
  }

  .dropdown-wrapper {
    display: flex;
    gap: 10px;
    margin-bottom: 20px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
  }

  th,
  td {
    border: 1px solid #ccc;
    padding: 8px;
    text-align: left;
  }


   button {
    padding: 6px 12px;
    cursor: pointer;
    background-color: orangered;
    color: white;
    border: none;
    border-radius: 4px;
  }

  button:hover {
    background-color: orange;
  } 
button.remove-btn {
    background-color: crimson;
    color: white;
    border: none;
  }

</style>
