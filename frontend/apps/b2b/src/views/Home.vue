<template>
	<BaseLayout>
		<template #body>
			<div class="page-content">
				<!-- Hero banner -->
				<HeroBanner />
				<section class="w-full p-2 flex flex-col gap-4">
					<!-- Search bar -->
					<SearchBar />
					<!-- Feature massage bar -->
					<FeatureMessageBar />
					<!-- Feature nav bar -->
					<FeatureNavBar />
					<!-- Features section -->
					<FeatureSection />
				</section>
				<!-- Product section -->
				<section class="grid grid-cols-3 gap-2 px-2">
					<ProductThumb
						v-for="product in products.data"
						:key="product.name"
						:product="product"
					/>
				</section>
			</div>
		</template>
	</BaseLayout>
</template>

<script setup>
import HeroBanner from '@/components/HeroBanner.vue'
import BaseLayout from '@/components/layouts/BaseLayout.vue'
import FeatureMessageBar from '@/components/FeatureMessageBar.vue'
import FeatureNavBar from '@/components/FeatureNavBar.vue'
import SearchBar from '@/components/SearchBar.vue'
import FeatureSection from '@/components/FeatureSection.vue'
import ProductThumb from '@/components/ProductThumb.vue'

import { createResource } from 'frappe-ui'

const products = createResource({
    url: 'erpnext.api.item_api.home_items',
    params: {
        limit: 5
    },
    auto: true
})

</script>
