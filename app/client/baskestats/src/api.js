// api.js

export async function fetchTeams() {
  try {
    const response = await fetch('http://127.0.0.1:5003/teams');
    if (response.ok) {
      return await response.json();
    } else {
      console.error('Failed to fetch teams:', response.statusText);
      return [];
    }
  } catch (error) {
    console.error('Error fetching teams:', error);
    return [];
  }
}

export async function fetchMatches(cId) {
  try {
    const response = await fetch(`http://127.0.0.1:5005/championships/${cId}/matches`);
    if (response.ok) {
      return await response.json();
    } else {
      console.error('Failed to fetch matches:', response.statusText);
      return [];
    }
  } catch (error) {
    console.error('Error fetching matches:', error);
    return [];
  }
}