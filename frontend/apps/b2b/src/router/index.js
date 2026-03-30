import { createRouter, createWebHistory } from "@ionic/vue-router"

import TabbedViewHome from "../views/TabbedViewHome.vue"

const routes = [
    {
        path: "/",
        redirect: "/splash",
    },
    {
        path: "/splash",
        name: "Splash",
        component: () => import("@/views/SplashScreen.vue"),
    },
    {
        path: "/",
        component: TabbedViewHome,
        children: [
            {
                path: "",
                redirect: "/home",
            },
            {
                path: "/home",
                name: "Home",
                component: () => import("@/views/Home.vue"),
            },
            {
                path: "/products",
                name: "Products",
                component: () => import("@/views/Products.vue"),
            },
            {
                path: "/offers",
                name: "Offers",
                component: () => import("@/views/Offers.vue"),
            },
            {
                path: "/cart",
                name: "Cart",
                component: () => import("@/views/Cart.vue"),
            },
            {
                path: "/profile",
                name: "Profile",
                component: () => import("@/views/Profile.vue"),
            },
        ],
    },
    {
        path: "/product/:id",
        name: "ProductDetail",
        component: () => import("@/views/ProductDetail.vue"),
    },
    {
        path: "/category/:name",
        name: "CategoryProducts",
        component: () => import("@/views/CategoryProducts.vue"),
    },
    {
        path: "/wishlist",
        name: "Wishlist",
        component: () => import("@/views/Wishlist.vue"),
    },
    {
        path: "/checkout",
        name: "Checkout",
        component: () => import("@/views/Checkout.vue"),
    },
    {
        path: "/order-success",
        name: "OrderSuccess",
        component: () => import("@/views/OrderSuccess.vue"),
    },
    {
        path: "/orders",
        name: "OrderHistory",
        component: () => import("@/views/OrderHistory.vue"),
    },
    {
        path: "/order-detail/:id",
        name: "OrderDetail",
        component: () => import("@/views/OrderDetail.vue"),
    },
    {
        path: "/reorder/:id",
        name: "Reorder",
        component: () => import("@/views/Reorder.vue"),
    },
    {
        path: "/request-medicine",
        name: "RequestMedicine",
        component: () => import("@/views/RequestMedicine.vue"),
    },
    {
        path: "/notifications",
        name: "Notifications",
        component: () => import("@/views/Notifications.vue"),
    },
    {
        path: "/notification-detail/:id",
        name: "NotificationDetail",
        component: () => import("@/views/NotificationDetail.vue"),
    },
    {
        path: "/offer-detail/:id",
        name: "OfferDetail",
        component: () => import("@/views/OfferDetail.vue"),
    },
    {
        path: "/about",
        name: "AboutUs",
        component: () => import("@/views/AboutUs.vue"),
    },
    {
        path: "/terms",
        name: "Terms",
        component: () => import("@/views/Terms.vue"),
    },
    {
        path: "/contact",
        name: "Contact",
        component: () => import("@/views/Contact.vue"),
    },
    {
        path: "/contact-list",
        name: "ContactList",
        component: () => import("@/views/ContactList.vue"),
    },
    {
        path: "/contact-detail/:id",
        name: "ContactDetail",
        component: () => import("@/views/ContactDetail.vue"),
    },
    {
        path: "/follow-us",
        name: "FollowUs",
        component: () => import("@/views/FollowUs.vue"),
    },
    {
        path: "/leaderboard",
        name: "Leaderboard",
        component: () => import("@/views/Leaderboard.vue"),
    },
    {
        path: "/settings",
        name: "Settings",
        component: () => import("@/views/Settings.vue"),
    },

    {
        path: "/login",
        name: "Login",
        component: () => import("@/views/Login.vue"),
    },
]

const router = createRouter({
    history: createWebHistory("/b2b"),
    routes,
})

export default router
