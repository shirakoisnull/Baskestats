<script>
  import { navigate } from "svelte-routing";
  // @ts-ignore
  import { onMount } from "svelte";
  import SecretaryPanel from "./SecretaryPanel.svelte";

  let username = "";
  let password = "";
  let isAuthenticated = false; // Track user authentication status
  let storedUsername = "";

  async function handleSubmit() {
    try {
      const response = await fetch("http://127.0.0.1:5001/login", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const contentType = response.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
          const responseData = await response.json();
          if (responseData.token && responseData.username) {
            const { token, username } = responseData;
            localStorage.setItem("jwtToken", token);
            localStorage.setItem("username", username);
            // isAuthenticated = true;
            // storedUsername = username;

            // If login is successful, navigate to SecretaryPanel
            navigate("/secretary");
          } else {
            alert("Unexpected response format");
          }
        } else {
          const errorMessage = await response.text();
          if (errorMessage === "Error") {
            alert("Invalid credentials");
          } else {
            alert("Unexpected error");
          }
        }
      } else {
        console.error("Error:", response.status);
        alert("Failed to log in");
      }
    } catch (error) {
      console.error("Error:", error);
      alert("An error occurred while logging in");
    }
  }

  onMount(() => {
    const token = localStorage.getItem("jwtToken");
    if (token) {
      isAuthenticated = true;
    }
  });
</script>

<!-- {#if isAuthenticated} -->
<!-- If authenticated, render the authenticated page -->
<!-- TODO: add routing -->
<!-- <SecretaryPanel /> -->
<!-- {:else} -->
<!-- If not authenticated, render the login form -->
<div class="card">
<form on:submit|preventDefault={handleSubmit} class="login">
  <label>
    <p>Username:</p>
    <input type="text" bind:value={username} />
  </label>
  <label>
    <p>Password:</p>
    <input type="password" bind:value={password} />
  </label>
  <button type="submit">Login</button>
</form>
</div>
<!-- {/if} -->
