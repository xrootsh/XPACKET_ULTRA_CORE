const target = process.argv[2] || "Target";

// ഡാഷ്‌ബോർഡിലേക്ക് ഡാറ്റ അയക്കാനുള്ള ഫംഗ്ഷൻ
async function updateDashboard(user, status) {
    try {
        await fetch('http://localhost:9000/update', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ target: user, status: status, engine: "X-ROOT" })
        });
    } catch (error) { }
}

console.clear();
console.log("\x1b[31m======================================================\x1b[0m");
console.log("    \x1b[37m✖️\x1b[31m🔴\x1b[37m 𝗜𝗡𝗜𝗧𝗜𝗔𝗧𝗜𝗡𝗚 𝗫-𝗥𝗢𝗢𝗧 𝗘𝗡𝗚𝗜𝗡𝗘 \x1b[37m[REAL OSINT]\x1b[0m");
console.log("\x1b[31m======================================================\x1b[0m\n");
console.log(` \x1b[36m[*] REAL-TIME HUNTING IDENTITY:\x1b[37m ${target}\x1b[0m\n`);

updateDashboard(target, "OSINT HUNT STARTED");

const sites = {
    "GitHub": `https://github.com/${target}`,
    "Reddit": `https://www.reddit.com/user/${target}/about.json`
};

console.log(" \x1b[32m[+] STAGE 1: Executing Live Network Requests...\x1b[0m\n");

async function hunt() {
    for (const [site, url] of Object.entries(sites)) {
        try {
            updateDashboard(target, `SCANNING ${site.toUpperCase()}`);
            const res = await fetch(url, { method: 'GET', headers: { 'User-Agent': 'Mozilla/5.0' } });
            if (res.status === 200) {
                console.log(`   \x1b[32m[+] FOUND [${site}]:\x1b[36m ${url}\x1b[0m`);
            } else if (res.status === 404) {
                console.log(`   \x1b[31m[-] Not Found [${site}]\x1b[0m`);
            }
        } catch (err) {
            console.log(`   \x1b[31m[!] Connection Error [${site}]\x1b[0m`);
        }
    }
    updateDashboard(target, "HUNT COMPLETE");
    console.log("\n \x1b[31m[!] X-ROOT LIVE HUNT COMPLETE.\x1b[0m\n");
}

hunt();
