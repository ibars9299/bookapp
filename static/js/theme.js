function toggleTheme() {
    const theme = localStorage.getItem('theme') === 'dark' ? 'light' : 'dark';
    localStorage.setItem('theme', theme);
    document.documentElement.setAttribute('data-theme', theme);
}

// Sayfa yüklendiğinde tema kontrolü
document.addEventListener('DOMContentLoaded', () => {
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
}); 