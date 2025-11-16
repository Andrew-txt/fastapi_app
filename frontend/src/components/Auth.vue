<template>
    <h1>suck ma dih</h1>
    <div v-if="message" class="message">{{ message }}</div>
    <div class="profile-section">
        <img v-if="picUrl" :src="picUrl" class="avatar" />
        <div v-if="userName" class="username">
            Welcome, <strong>{{ userName }}</strong>.
        </div>

    </div>
</template>


<script>
export default {
    data() {
        return {
            message:'',
            userName: '',
            picUrl: '',
        };
    },
    mounted() {
        const queryParams = new URLSearchParams(window.location.search)
        const code = queryParams.get('code')
        if (code) {
            fetch('http://localhost:8000/auth/google/callback', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ code: code }),
            })
            .then(res => {
                if (!res.ok) {
                    throw new Error('Server Error')
                }
                return res.json()
            })
            .then(data => {
                this.picUrl = data.user.picture
                data.email
                this.userName = data.user.name
            })
        } else {
            this.message = 'No "code" parameter';
        }
    },
};
</script>