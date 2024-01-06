<script>
  import { fetchTeams, viewTeam } from "../api.js";
  import { onMount } from "svelte";
  import BottomNavigation from "../BottomNavigation.svelte";
  import TeamModal from "../modals/TeamModal.svelte";

  let teams = [];
  let searchQuery = '';
  let showModal = false;
  let teamInfo = [];

  onMount(async () => {teams = await fetchTeams();});

async function handleView(tId){
  teamInfo = await viewTeam(tId);
   showModal = true;
  }

  $: visibleTeams = searchQuery ?
    teams.filter(team => {
      return (
        team[1].toLowerCase().includes(searchQuery.toLowerCase())
        // Replace 'team.name' with the property you want to filter/search by
      );
    }) : teams;

</script>

{#if showModal}
  <TeamModal
    {showModal}
    results={teamInfo}
    closeModal={() => (showModal = false)}
  />
{/if}

<BottomNavigation />
<input type="text" bind:value={searchQuery} placeholder="Search teams..." />
<table>
  <thead>
    <tr>
      <th>Name</th>
      <!-- <th>City</th>
      <th>Wins</th>
      <th>Losses</th> -->
      <th>Actions</th>
    </tr>
  </thead>
  <tbody>
    {#each visibleTeams as team}
      <tr>
        <td>{team[1]}</td>
        <!-- <td>{team[2]}</td>
        <td>{team[3]}</td>
        <td>{team[4]}</td> -->
        <td>
            <button on:click={() => handleView(team[0])}>Info</button>
        </td>
      </tr>
    {/each}
  </tbody>
</table>