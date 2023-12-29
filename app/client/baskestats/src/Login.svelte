<script>
  // @ts-ignore
  import { onMount } from 'svelte';
  import SecretaryPanel from './SecretaryPanel.svelte';

  let username = '';
  let password = '';
  let isAuthenticated = false; // Track user authentication status

  async function handleSubmit() {
    try {
      const response = await fetch('http://127.0.0.1:5001/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const { token } = await response.json();
        localStorage.setItem('jwtToken', token); // Store token in localStorage
        isAuthenticated = true;
      } else {
        alert('Invalid credentials');
      }
    } catch (error) {
      console.error('Error:', error);
    }
  }

  onMount(() => {
    const token = localStorage.getItem('jwtToken');
    if (token) {
      isAuthenticated = true;
    }
  });

</script>

{#if isAuthenticated}
  <!-- If authenticated, render the authenticated page -->
  <SecretaryPanel />
{:else}
  <!-- If not authenticated, render the login form -->
  <form on:submit|preventDefault={handleSubmit}>
    <label>
      Username:
      <input type="text" bind:value={username} />
    </label>
    <label>
      Password:
      <input type="password" bind:value={password} />
    </label>
    <button type="submit">Login</button>
  </form>
{/if}

<!-- Create the AuthenticatedPage component -->

<!-- <form on:submit|preventDefault={handleSubmit}>
  <label>
    Username:
    <input type="text" bind:value={username} />
  </label>
  <label>
    Password:
    <input type="password" bind:value={password} />
  </label>
  <button type="submit">Login</button>
</form> -->