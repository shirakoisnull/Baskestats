<script>
  import ConfirmationModal from "../ConfirmationModal.svelte";
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  let showModal = false;
  let selectedTeam = null;
  // Assuming teamsData contains your team entries, fetched from somewhere
  let playerData= [
    { id: 1, name: "Team A", city: "City A", wins: 5, losses: 2 },
    { id: 2, name: "Team B", city: "City B", wins: 3, losses: 4 },
    // Add more entries as needed
  ];
  // Initialize teams as an empty array
  let teams = [];

  // Fetch teams data from the backend
  async function fetchTeams() {
    try {
      const response = await fetch("http://127.0.0.1:5003/teams"); // Replace with your API endpoint
      if (response.ok) {
        const teamData = await response.json();

        // Assuming the structure is [[team_id, team_name, team_city, team_wins, team_losses], ...]
        teams = teamData.map((team) => ({
          id: team[0],
          name: team[1],
          city: team[2],
          wins: team[3],
          losses: team[4],
        }));

        // teams array assumed to be an array of objects with specific properties for each team
      } else {
        console.error("Failed to fetch teams:", response.status);
        // Handle error
      }
    } catch (error) {
      console.error("Error fetching teams:", error);
      // Handle error
    }
  }

  // Fetch teams data on component mount
  onMount(fetchTeams);

  function handleClick(event) {
    // Handle the click event here
    console.log("Button clicked!");
    // window.location.href = "/teamcreate";
    navigate("/teamcreate");
  }
  function deleteTeam(team) {
    selectedTeam = team;
    showModal = true;
  }
  // Function to handle delete confirmation
  // function confirmDelete(id) {
  //   const confirmation = confirm("Are you sure you want to delete this entry?");
  //   if (confirmation) {
  //     // Implement logic to delete the entry with the given ID
  //     teamsData = teamsData.filter((team) => team.id !== id);
  //   }
  // }
  function handleConfirmDelete(confirm) {
    if (confirm) {
      // Implement deletion logic
      // teamsData = teamsData.filter((team) => team.id !== id);
      console.log("Deleted:", selectedTeam);
      // Perform actual deletion operation here

      // After deletion or on cancel, hide the modal
      showModal = false;
    } else {
      // On cancel, hide the modal
      showModal = false;
    }
  }
  function handleUpdate(team) {
    navigate(`/teamupdate`, { state: { team } });
  }
</script>

{#if showModal}
  <ConfirmationModal teamName={selectedTeam.name} on:confirm={handleConfirmDelete} />
{/if}

<h1>Team Management</h1>

<div>
  <button on:click={handleClick}>Create New Team</button>
</div>

<table>
  <thead>
    <tr>
      <th>ID</th>
      <th>Name</th>
      <th>City</th>
      <th>Wins</th>
      <th>Losses</th>
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each teamsData as team}
      <tr>
        <td>{team.id}</td>
        <td>{team.name}</td>
        <td>{team.city}</td>
        <td>{team.wins}</td>
        <td>{team.losses}</td>
        <td>
          <!--  <button on:click={() => {
            // Redirect to team update page (Replace with your routing logic)
            // Example: window.location.href = `/teamupdate/${team.id}`;
            console.log(`Redirect to team update for ID: ${team.id}`);
          }}>Update</button> -->
          <button on:click={() => handleUpdate(team)}>Update</button>
          <button on:click={() => deleteTeam(team)}>Delete</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<style>
  table {
    width: 100%;
    border-collapse: collapse;
    margin: auto; /* Center the table horizontally */
  }

  th,
  td {
    padding: 10px;
    border: 1px solid #ccc;
    text-align: left;
  }

  th {
    /* background-color: #f2f2f2; */
    font-weight: bold;
  }

  tr:hover {
    background-color: #e9e9e921;
  }

  /* Style for update and delete buttons */
  button {
    padding: 6px 10px;
    margin: 2px;
    cursor: pointer;
    color: white;
    /* border: none; */
    border-radius: 4px;
  }
</style>
