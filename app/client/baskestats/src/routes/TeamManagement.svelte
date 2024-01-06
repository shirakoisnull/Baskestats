<script>
  // import ConfirmationModal from "../ConfirmationModal.svelte";
  import { onMount } from "svelte";
  import { navigate } from "svelte-routing";

  // let showModal = false;
  // let selectedTeam = null;


  // BEGIN REQUEST FROM API
  // Initialize teams as an empty array
  let teams = [];
  let searchQuery = '';

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
    navigate("/teamcreate");
  }

  async function deleteTeam(team) {
    const confirmation = window.confirm(
      `Are you sure you want to delete ${team.name}?`
    );
    if (confirmation) {
      // IMPLEMENT DELETION LOGIC
      try {
        const response = await fetch(`http://127.0.0.1:5003/teams/${team.id}`, {
          method: "DELETE",
        });

        if (response.ok) {
          fetchTeams();
          console.log("Team deleted successfully!");
          alert(`Deleted ${team.name}`);
          // Perform any necessary actions upon successful deletion
          // For example, update the UI or reload team list
        } else {
          console.error("Failed to delete team:", response.statusText);
          // alert("POU PA RE KARAMHTRO?");
          alert("Cannot delete a team in use!")
        }
      } catch (error) {
        console.error("Error deleting team:", error);
      }
    }
  }

  // THE CURSED CONFIRMATION MODAL THAT NEVER WORKS
  // function deleteTeam(team) {
  //     selectedTeam = team;
  //     showModal = true;
  //   }
  // function handleConfirmDelete(confirm) {
  //     confirmed = confirm; // Receive confirmation status
  //     if (confirmed) {
  //       teamsData = teamsData.filter(team => team.id !== selectedTeam.id);
  //       showModal = false;
  //     }
  //     showModal = false;
  //   }

  function handleUpdate(team) {
    navigate(`/teamupdate`, { state: { team } });
  }
  // ################# SEARCH BY NAME #####################
 // Filtered teams based on search query
  $: visibleTeams = searchQuery ?
    teams.filter(team => {
      return (
        team.name.toLowerCase().includes(searchQuery.toLowerCase())
        // Replace 'team.name' with the property you want to filter/search by
      );
    }) : teams;
</script>

<!-- {#if showModal}
  <ConfirmationModal teamName={selectedTeam.name} on:confirm={handleConfirmDelete} />
{/if} -->

<h1>Team Management</h1>

<input type="text" bind:value={searchQuery} placeholder="Search teams..." />

<!-- <div class="card"> -->
  <button on:click={handleClick}>Create New Team</button>
<!-- </div> -->

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
    {#each visibleTeams as team}
      <tr>
        <td>{team.id}</td>
        <td>{team.name}</td>
        <td>{team.city}</td>
        <td>{team.wins}</td>
        <td>{team.losses}</td>
        <td>
          <button on:click={() => handleUpdate(team)}>Update</button>
          <button class="delete-button" on:click={() => deleteTeam(team)}
            >Delete</button
          >
          <!-- <button on:click={() => deleteTeam(team)} class="delete-button">Delete</button> -->
        </td>
      </tr>
    {/each}
  </tbody>
</table>

<button class="back-button" on:click={() => navigate("/secretary")}>Go Back</button>

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
  /* Style the back button */
  .back-button {
    position: absolute;
    top: 20px;
    left: 20px;
    padding: 10px;
    background-color: #ff4000;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
   }
</style>
